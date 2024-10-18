from IPython.display import display, HTML

html_code = '''
<!DOCTYPE html>
<html>
<body>
  <script src="https://d3js.org/d3.v6.min.js"></script>
  <script>
    const dataset = [
                  [ 34,    78 ],
                  [ 109,   280 ],
                  [ 310,   120 ],
                  [ 79,    411 ],
                  [ 420,   220 ],
                  [ 233,   145 ],
                  [ 333,   96 ],
                  [ 222,   333 ],
                  [ 78,    320 ],
                  [ 21,    123 ]
                ];

    const w = 500;
    const h = 500;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    // Append circles
    svg.selectAll("circle")
       .data(dataset)
       .enter()
       .append("circle")
       .attr("cx", d => d[0])
       .attr("cy", d => h - d[1])  // Invert the y-axis
       .attr("r", 5);

    // Append text labels
    svg.selectAll("text")
       .data(dataset)
       .enter()
       .append("text")
       .attr("x", d => d[0] + 5)  // Offset by 5 units
       .attr("y", d => h - d[1])  // Match the circle's cy value
       .text(d => `${d[0]}, ${d[1]}`)
       .attr("font-size", "10px") // Optional: Set font size
       .attr("fill", "black");    // Optional: Set text color

  </script>
</body>
</html>
'''

# Display the HTML code to the user
display(HTML(html_code))
