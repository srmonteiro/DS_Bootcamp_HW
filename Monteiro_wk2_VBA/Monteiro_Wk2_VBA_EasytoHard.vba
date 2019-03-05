Sub IBroketheHardcodesonowIhavetostartover()

    'Create Dimensions for all variables and loops
    '_________________________________
    
        'Dims so we can loop
        '_________________________________
        
            Dim i As Long
            Dim lastRow As Long
            
        'Dims for the variables we seek to analyze
        '_________________________________
        
            Dim Company_Ticker As String
            Dim Company_Total_Volume As Double
            
            Dim Summary_Table_Row As Long
            
    
    'Create container For Loop to Cycle through the Worksheets
    '_________________________________
    
        For Each ws In Worksheets
        
            Summary_Table_Row = 2
            Company_Total_Volume = 0
            
             'Create Column Headers for Summary Table on Each Worksheet
            '_________________________________
            
                    ws.Cells(1, 9).Value = "Ticker"
                    ws.Cells(1, 10).Value = "Yearly Change"
                    ws.Cells(1, 11).Value = "Percent Change"
                    ws.Cells(1, 12).Value = "Total Stock Volume"
                    
                    
                        ' Reset the Row Count for the nested For Loop analyzing each company
                        '_________________________________
        
                            lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
                               ' MsgBox (lastRow)
                               
                        ' Nested For Loop analyzing each company
                        '_________________________________
                        
                            For i = 2 To lastRow
                            
                                If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                                
                                    Company_Ticker = ws.Cells(i, 1).Value
                                    ws.Cells(Summary_Table_Row, 9).Value = Company_Ticker
                                    
                                    Company_Total_Volume = Company_Total_Volume + ws.Cells(i, 7).Value
                                    ws.Cells(Summary_Table_Row, 12).Value = Company_Total_Volume
                                    
                                   ' Company_Total_Volume = Company_Total_Volume + ws.Cells(i, 7).Value
                                   ' ws.Cells(Summary_Table_Row, 12).Value = Company_Total_Volume
                                    
                                    Summary_Table_Row = Summary_Table_Row + 1
                                    Company_Total_Volume = 0
                                    
                                Else
                                    
                                   Company_Total_Volume = Company_Total_Volume + ws.Cells(i, 7).Value
                                        ' MsgBox (Company_Total_Volume)
                                    
                                  
                                    
                                End If
                                    
                            
                            Next i
                                        
        
        Next ws
    
    
    End Sub
    
