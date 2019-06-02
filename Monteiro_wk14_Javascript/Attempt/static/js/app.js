// ----------------------------------------------------------------------------
// Parking lot of reference info --> I have the memory of a goldfish right now

    // Classes

        //  filters         || line 31  
        //  form-control    || line 40, etc

    // Ids 

        //  filters         || line 37
        //  datetime        || line 44
        //  city            || line 52
        //  state           || line 48
        //  country         || line 52
        //  shape           || line 56
        //  filter-btn      || line 60
        //  ufo-table       || line 68 

// Select the UFO Table               
// var table = document.getElementById("ufo-table")

// ----------------------------------------------------------------------------

// My CODE HERE! 

// ----------------------------------------------------------------------------

// HANDLES FOR INTIAL index.html PAGE

// from data.js
var tableData = data;

// Select the table body
var tbody = d3.select("tbody");

// ----------------------------------------------------------------------------

// MAKE THE tableData APPEAR ON THE PAGE BEFORE ANY QUERIES ARE ENTERED

// ----------------------------------------------------------------------------

// Query tableData for each sighting
tableData.forEach(sighting => {

    // Query tableData for the Sighting
    // Console Log Data in json like format
    console.log(sighting);

    // Create new row in table body
    var row = tbody.append("tr");
    
    // Query tableData for the Sighting
    // Thanks Karen! I couldn't get the table 
    // to load right without mixing the syntax style
    Object.entries(sighting).forEach(function([key, value]) {

        // Append a cell to the row for each value in the Sighting
        var cell = row.append("td");

        cell.text(value);
    });
});

// ----------------------------------------------------------------------------

// Handles for the filter and query 

// ----------------------------------------------------------------------------

// Select the filters from the Query Form
var filters = d3.select('#filters')

// Select filter button
var filter_btn = d3.select("#filter-btn");

// On click, generate new table with filter query
filter_btn.on("click", function(){

    // Don't reload the page unless button is clicked 
    d3.event.preventDefault();

    // Select query terms from the form
    var dateQuery = d3.select("#datetime").select('input');
    var dateValue = dateQuery.property("value");  
    var cityQuery = d3.select("#city").select('input').value;
    var stateQuery = d3.select("#state").select('input').value;
    var countryQuery = d3.select("#country").select('input').value;
    var shapeQuery = d3.select("#shape").select('input').value;

    // console.log the query terms
    var queryTerms = { "Date" : dateQuery, 
                  "City" : cityQuery, 
                  "State" : stateQuery, 
                  "Country" : countryQuery,
                  "Shape" : shapeQuery}
    console.log(queryTerms);

    if (queryTerms.dateValue == '') {
        var queryResults = tableData;
        }
    else {
        var queryResults = tableData.filter(sighting => sighting.datatime == dateValue);
        }



    // Add the filtered data to the table body
    queryResults.forEach(sighting => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(function([key, value]) {
            var cell = row.append("td");
            cell.text(value);
        })
    });

    // Clear the query terms
    document.getElementById("datetime").value = '';
    document.getElementById("city").value = '';
    document.getElementById("state").value = '';
    document.getElementById("country").value = '';
    document.getElementById("shape").value = '';
        
  });

