#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(gghalves)
source("script/helper.R")
theme_set(theme_classic())

# The palette with black:
cbPalette <- c("#E69F00", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#56B4E9", "#CC79A7", "#000000")

function(input, output, session) {
  
    # create response data 
    data_resp <- reactive({
      data %>%
        filter(expt %in% input$selectExpt) %>%
        filter(`Trial Type` %in% input$selectTrialType) %>%
        group_by(`Subject ID`, expt, `Trial Type`) %>%
        summarise(mean_resp = mean(response_yes))
    })
    
    # create categorization data
    data_cat <- reactive({
      data %>% 
        filter(`Trial Type` %in% c("1_Disjunct_True", "2_Disjunct_True")) %>%
        group_by(`Subject ID`, expt, `Trial Type`) %>%
        summarise(sum_resp_yes = length(response_yes[response_yes == 1]), 
                  sum_resp_no = length(response_yes[response_yes == 0])) %>%
        pivot_wider(names_from = `Trial Type`, values_from = c(sum_resp_yes, sum_resp_no)) %>%
      mutate(child_type = case_when(
        sum_resp_yes_1_Disjunct_True >= input$threshold 
          & sum_resp_yes_2_Disjunct_True >= input$threshold ~ "inclusive",
        sum_resp_no_1_Disjunct_True >= input$threshold 
          & sum_resp_yes_2_Disjunct_True >= input$threshold ~ "conjunctive",
        sum_resp_yes_1_Disjunct_True >= input$threshold 
          & sum_resp_no_2_Disjunct_True >= input$threshold ~ "exclusive",
        .default = "other"
      ))
    })
    
    #### RESPONSE TAB ####
    output$respTable <- renderTable(data_resp() %>%
                                  group_by(expt, `Trial Type`) %>%
                                  summarise(`Proportion Response 'Yes'` = mean(mean_resp)) %>%
                                  rename(Experiment = expt))
    
    output$respPlot <- renderPlot({
        ggplot(data = data_resp(), 
               mapping = aes(x = `Trial Type`, 
                             y = mean_resp, 
                             color = expt,
                             fill = expt,
                             group = expt)) + 
        stat_summary(fun.data = "mean_cl_boot", 
                      geom = "pointrange", 
                     position = position_dodge(width = 0.5)) + 
        stat_summary(fun = "mean",
                     geom = "line", 
                     aes(group = expt),
                     position = position_dodge(width = 0.5)) + 
        geom_half_violin(data = data_resp() %>%
                           filter(expt == "Replication"),
                         aes(group = `Trial Type`),
                         position = position_nudge(x = -.1, y = 0),
                         side = "l", 
                         alpha = 0.5,
                         # wanted to make this match the experiment, but
                         # it didn't work...
                         #fill = "#E69F00" 
                         ) +
        geom_half_violin(data = data_resp() %>%
                           filter(expt == "Three Alternatives"),
                         aes(group = `Trial Type`),
                         position = position_nudge(x = .1, y = 0),
                         side = "r", 
                         alpha = 0.5, 
                         #fill = "#009E73"
                         ) +
        geom_hline(yintercept = 0.5, 
                   linetype = "dashed") + 
        coord_cartesian( # to make sure I don't cut off anything
          ylim = c(0,1)
        ) +
        scale_color_manual(values=cbPalette) + 
        scale_fill_manual(values=cbPalette) + 
        theme(text = element_text(size = 15)) + 
        labs(y = "Proportion Responding 'Yes'", 
             color = "Experiment", 
             fill = "Experiment")
      })
        
      #### CATEGORIZATION TAB ####
      output$catTable <- renderTable(data_cat() %>%
                                       group_by(expt, child_type) %>%
                                       count() %>%
                                       mutate(n = as.character(n)) %>%
                                       pivot_wider(names_from = child_type,
                                                   values_from = n) %>%
                                      bind_rows(.,
                                        tibble(
                                          expt = "Tieu et al. (2017)",
                                          conjunctive = as.character(19),
                                          inclusive = as.character(14),
                                          exclusive = as.character(3),
                                          other = as.character(10)
                                        )
                                      ) %>%
                                      rename(Experiment = expt) %>%
                                      select(Experiment, inclusive, 
                                             exclusive, conjunctive, other)
                    )
      
      output$catPlot <- renderPlot({
        ggplot(data_cat(),
               aes(x = child_type, 
                   fill = expt)) + 
          geom_bar(position = position_dodge()) + 
          scale_fill_manual(values=cbPalette) + 
          theme(text = element_text(size = 15)) + 
          labs(y = "Count", 
               x = "Type of 'or' Interpretation",
               color = "Experiment", 
               fill = "Experiment")
      })
}
