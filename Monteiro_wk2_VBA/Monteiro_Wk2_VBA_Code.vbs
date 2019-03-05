Sub My_Genius_Stock_Analysis()

    ' Thank Yous & Acknowledgements
    ' ___________________________________
    
        ' A special shoutout to Alex Lecocq in our group, who not only was the only one to solve this problem, but also
        ' patiently walked the rest of our group through his logic and code so that we had a better grasp of the material.
        ' I certainly would not have been able to achieve nearly as complete a project without his assistance.
        ' I'm still not precisely certain why it works, but naming the worksheets was a big help and I didn't try
        ' Do While loops until Alex explained why For Loops posed problems
    
    ' Define Necessary Dimensions and Variables
    ' ___________________________________
    
        ' Dims for Loops
        '_____________________
        
            'Dims for Do While Loops on each sheet to cycle through company data
            '_____________________
          
                Dim i As Long
                Dim j As Long
                Dim ws As Worksheet
            
            'Dim for For Loop to cycle through each sheet to cycle through company data
            '_____________________
            
                Dim n As Long
            
        'Dims for Variables and Values in the Summary Tables
        '_____________________
        
            'Dims for Companies
            '_____________________
            
                Dim Company_Ticker As String
                Dim Company_Number As Long
            
            'Dims for Calculating Summary Figues
            '_____________________
            
                Dim Stock_Volume As Double
                Dim First_Day_Close_Value As Double
                Dim Last_Day_Close_Value As Double
                
            'Dims for Summary Figues
            '_____________________
            
                Dim Comp_Yearly_Change As Double
                Dim Comp_Percent_Change As Double
                Dim Comp_Total_Stock_Volume As Double
                
            'Dims for Highlight Table Figues
            '_____________________
            
                Dim Greatest_Percent_Increase_Value As Double
                Dim Greatest_Percent_Increase_Ticker As String
                Dim Greatest_Percent_Decrease_Value As Double
                Dim Greatest_Percent_Decrease_Ticker As String
                Dim Greatest_Percent_Total_Value As Double
                Dim Greatest_Percent_Total_Ticker As String
                
            'Defining Sheets so For Loop can cycle through sheets (I hope...)
            '_____________________
            
                Dim WorksheetName(3) As String
                
                    WorksheetName(0) = "2016"
                    WorksheetName(1) = "2015"
                    WorksheetName(2) = "2014"
                    
            'Setting Conditional formatting on each sheet for Yearly Change
            '_____________________
            
                Dim rg As Range
                Dim cond1 As FormatCondition, cond2 As FormatCondition, cond3 As FormatCondition
                Set rg = Range("J2", Range("J2").End(xlDown))
                 
            'define the rule for each conditional format
            '_____________________
            
                Set cond1 = rg.FormatConditions.Add(xlCellValue, xlGreater, "0")
                Set cond2 = rg.FormatConditions.Add(xlCellValue, xlLess, "0")
                Set cond3 = rg.FormatConditions.Add(xlCellValue, xlEqual, "0")
                 
                With cond1
                .Interior.Color = vbGreen
                .Font.Color = vbBlack
                End With
                 
                With cond2
                .Interior.Color = vbRed
                .Font.Color = vbBlack
                End With
                 
                With cond3
                .Interior.Color = vbWhite
                .Font.Color = vbBlack
                End With
                 
                 
    ' Container For Loop to cycle through Worksheets
    '__________________________________________________
    
    For n = 0 To 2
    
        ' Resets the values of arguments and functions that have sheet specific info after the nested Do While Loop
        '__________________________________________________
        
            Company_Number = 1
            i = 2
            Greatest_Percent_Increase_Value = 0
            Greatest_Percent_Increase_Ticker = ""
            Greatest_Percent_Decrease_Value = 0
            Greatest_Percent_Decrease_Ticker = ""
            Greatest_Total_Value = 0
            Greatest_Total_Ticker = ""
    
        ' Add Labels to Column Headers on the Summary Table for Each Sheet
        ' ____________________________________
        
             Worksheets(WorksheetName(n)).Cells(1, 9).Value = "Ticker"
             Worksheets(WorksheetName(n)).Cells(1, 10).Value = "Yearly Change"
             Worksheets(WorksheetName(n)).Cells(1, 11).Value = "Percent Change"
             Worksheets(WorksheetName(n)).Cells(1, 12).Value = "Total Stock Volume"
    
        ' Add Labels to Column Headers and Row Names on the Highlight Tables for Each Sheet
        ' ____________________________________
        
             Worksheets(WorksheetName(n)).Cells(1, 15).Value = "Ticker"
             Worksheets(WorksheetName(n)).Cells(1, 16).Value = "Value"
             Worksheets(WorksheetName(n)).Cells(2, 14).Value = "Greatest % increase"
             Worksheets(WorksheetName(n)).Cells(3, 14).Value = "Greatest % Decrease"
             Worksheets(WorksheetName(n)).Cells(4, 14).Value = "Greatest total volume"
    
        ' Begin Outermost Do While Loop to cycle through Companies on each sheet and pipe information
        ' into the Summary Table
        ' ____________________________________
    
            Do While Worksheets(WorksheetName(n)).Cells(i, 1) <> ""
            
                Company_Ticker = Worksheets(WorksheetName(n)).Cells(i, 1)
                First_Day_Close_Value = Worksheets(WorksheetName(n)).Cells(i, 3)
                Stock_Volume = Worksheets(WorksheetName(n)).Cells(i, 7)
                i = i + 1
                
                    ' Nested Do While Loop to calculate figures for each company, then move on to next company
                    '____________________________________
                
                        Do While Worksheets(WorksheetName(n)).Cells(i, 1).Value = Worksheets(WorksheetName(n)).Cells(i - 1, 1)
                            
                            ' Add Each Day's Stock Volume to the Total Stock Value of the Company Ticker,
                            ' until we get to the next Company
                            '____________________________________
                    
                                Stock_Volume = Stock_Volume + Worksheets(WorksheetName(n)).Cells(i, 7)
                       
                            ' This If Conditional corrects for companies that start trading after Jan 1
                            ' Here's another moment where Alex was pivotal
                            '____________________________________
                        
                                If First_Day_Close_Value = 0 And Worksheets(WorksheetName(n)).Cells(i, 3) <> 0 Then
                                    First_Day_Close_Value = Worksheets(WorksheetName(n)).Cells(i, 3)
                                End If
                               
                            ' Move to the next row and start the While Loop over again
                            '____________________________________
                            
                            i = i + 1
            
                        Loop
                        
                    ' Snag the Last Day Close Value of the previous company (we have to look one line up!)
                    ' so we can calculate the Yearly Change
                    '____________________________________
                    
                          Last_Day_Close_Value = Worksheets(WorksheetName(n)).Cells(i - 1, 6)
                        
                    ' Now that we've cycled through every day of a Company,
                    ' print out the Company Ticker and the Yearly Change into the Summary Table
                    '____________________________________
                
                        Company_Number = Company_Number + 1
                        Worksheets(WorksheetName(n)).Cells(Company_Number, 9) = Company_Ticker
                        Worksheets(WorksheetName(n)).Cells(Company_Number, 10) = Last_Day_Close_Value - First_Day_Close_Value
                        
                    ' Correcting for when the company never traded
                    '___________________________________
                    
                        If First_Day_Close_Value <> 0 Then
                            Worksheets(WorksheetName(n)).Cells(Company_Number, 11) = (Last_Day_Close_Value - First_Day_Close_Value) / First_Day_Close_Value
                            
                            If (Last_Day_Close_Value - First_Day_Close_Value) / First_Day_Close_Value > Greatest_Percent_Increase_Value Then
                                Greatest_Percent_Increase_Value = (Last_Day_Close_Value - First_Day_Close_Value) / First_Day_Close_Value
                                Greatest_Percent_Increase_Ticker = Company_Ticker
                                
                            ElseIf (Last_Day_Close_Value - First_Day_Close_Value) / First_Day_Close_Value < Greatest_Percent_Decrease_Value Then
                                Greatest_Percent_Decrease_Value = (Last_Day_Close_Value - First_Day_Close_Value) / First_Day_Close_Value
                                Greatest_Percent_Decrease_Ticker = Company_Ticker
                            End If
                            
                        Else
                        
                            Worksheets(WorksheetName(n)).Cells(Company_Number, 11) = 0
                            
                        End If
                        
                        Worksheets(WorksheetName(n)).Cells(Company_Number, 12) = Stock_Volume
                        
                        If Stock_Volume > Greatest_Total_Value Then
                            Greatest_Total_Value = Stock_Volume
                            Greatest_Total_Ticker = Company_Ticker
                        
                        End If
                        
            Loop
    
            Worksheets(WorksheetName(n)).Cells(2, 15) = Greatest_Percent_Increase_Value
            Worksheets(WorksheetName(n)).Cells(2, 16) = Greatest_Percent_Increase_Ticker
            Worksheets(WorksheetName(n)).Cells(3, 15) = Greatest_Percent_Decrease_Value
            Worksheets(WorksheetName(n)).Cells(3, 16) = Greatest_Percent_Decrease_Ticker
            Worksheets(WorksheetName(n)).Cells(4, 15) = Greatest_Total_Value
            Worksheets(WorksheetName(n)).Cells(4, 16) = Greatest_Total_Ticker
            
    Next n
    
    End Sub
