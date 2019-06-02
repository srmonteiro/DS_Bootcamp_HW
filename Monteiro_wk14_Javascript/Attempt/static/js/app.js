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

// --------------------------------------

// My CODE HERE! 

// --------------------------------------

// GET A HANDLE ON EVERYTHING

// from data.js
var tableData = data;

// Select the table body
var tbody = d3.select("tbody");

// Select the filters from the Query Form
var filters = d3.select('#filters')

// Select filter button
var queryButton = d3.select("#filter-btn");

// --------------------------------------

// MAKE THE tableData APPEAR ON THE PAGE BEFORE ANY QUERIES ARE ENTERED

// Query tableData for each sighting
tableData.forEach(sighting => {

    // Query tableData for the Sighting
    // Console Log Data in json like format
    console.log(sighting);

    // Create new row in table body
    var row = tbody.append("tr");
    
    // Query tableData for the Sighting
    Object.entries(sighting).forEach(function([key, value]) {

        // Append a cell to the row for each value in the Sighting
        var cell = row.append("td");

        cell.text(value);
    });
});

// --------------------------------------



// On click, generate new table with filter query
queryButton.on("click", function(){

    // Don't reload the page unless button is clicked 
    d3.event.preventDefault();

    // Clear the results when new search criteria are provided  -- > Thank you Amelia!
    var sightings = d3.selectAll("td");                                              
    sightings.remove();
    var observations = d3.selectAll("tr"); 
    observations.remove();

    // Select query terms from the form
    var form = d3.select(".form-control").node().value;
    var dateQuery = d3.select("#datetime").node().value;   
    var cityQuery = d3.select("#city").node().value;
    var stateQuery = d3.select("#state").node().value;
    var countryQuery = d3.select("#country").node().value;
    var shapeQuery = d3.select("#shape").node().value;

    // console.log the query terms
    var queryTerms = { "Date" : dateQuery, 
                  "City" : cityQuery, 
                  "State" : stateQuery, 
                  "Country" : countryQuery,
                  "Shape" : shapeQuery}
    console.log(queryTerms);


    // Clear the query terms
    document.getElementById("datetime").value = '';
    document.getElementById("city").value = '';
    document.getElementById("state").value = '';
    document.getElementById("country").value = '';
    document.getElementById("shape").value = '';
        
});








