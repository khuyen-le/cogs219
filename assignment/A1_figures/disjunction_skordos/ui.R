#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)

# Define UI for application
fluidPage(
    title = "Children's interpretation of 'or'",
    tags$h2("Children's interpretation of 'or'"),
    tags$div(
       tags$span("This Shiny app visualizes data from 
                  Skordos, D., Feiman, R., Bale, A., & Barner, D. (2020).
                  Do children interpret ‘or’conjunctively?.", 
                 tags$i("Journal of Semantics, 37"),
                 "(2), 247-267."),
       tags$a("https://doi.org/10.1093/jos/ffz022")
    ),
    br(),

    # Sidebar
    sidebarLayout(
        sidebarPanel(
            checkboxGroupInput(
              "selectExpt",
              "Show Experiment(s):",
              choices = list("Replication" = "Replication", "Three Alternatives" = "Three Alternatives"),
              selected = "Replication"
            ), 
            checkboxGroupInput(
              "selectTrialType",
              "Show Trial Type(s):",
              choices = list("1_Disjunct_True" = "1_Disjunct_True", 
                             "2_Disjunct_True" = "2_Disjunct_True", 
                             "0_Disjunct_True" = "0_Disjunct_True", 
                             "Control_True" = "Control_True", 
                             "Control_False" = "Control_False"),
              selected = c("1_Disjunct_True", "2_Disjunct_True")
            ), 
            sliderInput("threshold",
                        "Categorization Threshold:",
                        min = 0,
                        max = 4,
                        value = 3), 
            
      ),

      mainPanel(
        tabsetPanel(
          # plot responses
          tabPanel("Response", 
                   plotOutput("respPlot"), 
                   tableOutput('respTable')
                  ), 
          # plot categorization
          tabPanel("Categorization", 
                   plotOutput("catPlot"),
                   tableOutput('catTable')
                   )
        )
      )
    )
)
