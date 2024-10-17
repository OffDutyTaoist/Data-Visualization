<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    const w = 500;
    const h = 100;

    const svg = d3.select("body")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", (d, i) => i * 30)
       .attr("y", (d, i) => h - 3 * d)
       .attr("width", 25)
       .attr("height", (d, i) => 3 * d)
       .attr("fill", "navy")
       .attr("class", "bar")
       .append("title")  // Append title element under each rect
       .text(d => d);    // Display data value in the title

    svg.selectAll("text")
       .data(dataset)
       .enter()
       .append("text")
       .attr("x", (d, i) => i * 30)
       .attr("y", (d, i) => h - 3 * d - 3)
       .text(d => d)
       .attr("fill", "white")
       .attr("font-size", "12px")
       .attr("text-anchor", "middle")
       .attr("dx", "12.5");

  </script>

  <style>
    .bar {
      transition: fill 0.3s;
    }

    .bar:hover {
      fill: brown;
    }
  </style>
</body>
