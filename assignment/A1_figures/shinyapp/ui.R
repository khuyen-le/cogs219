#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)

# Define UI for application that draws a histogram
fluidPage(

    # Application title
    titlePanel("Do children interpret 'or' conjunctively?"),

    # Sidebar with a slider input for number of bins
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

        # Show a plot of the generated distribution
        mainPanel(
          tabsetPanel(
            tabPanel("Response", 
                     plotOutput("respPlot"), 
                     tableOutput('respTable')
                    ), 
            tabPanel("Categorization", 
                     plotOutput("catPlot"),
                     tableOutput('catTable'))
          )
        )
    )
)
