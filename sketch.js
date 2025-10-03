let colorPalette;

function setup() {
  createCanvas(600, 600);
  angleMode(DEGREES); // Use degrees for easier rotation calculations
  noLoop(); // Draw once, can redraw on mouse press if desired

  // Define a "newyellow" color palette: muted, earthy, slightly greenish yellows
  colorPalette = [
    color(255, 230, 150), // Pale sunny yellow
    color(255, 200, 80),  // Muted gold
    color(200, 160, 50),  // Earthy mustard
    color(180, 190, 100), // Desaturated olive-yellow
    color(150, 140, 70)   // Muted ochre
  ];
}

function draw() {
  background(240, 250, 230); // Light, neutral background

  translate(width / 2, height / 2); // Center the succulent

  // Generative properties for this succulent instance
  let numLayers = floor(random(6, 11)); // Number of leaf layers
  let layerSpreadFactor = random(0.8, 1.2); // How much layers grow outwards
  let baseLeafLength = random(40, 60);
  let baseLeafWidth = random(15, 25);
  let layerRotationOffset = random(15, 35); // Initial twist for the first layer, and offset per layer
  let baseLeavesPerLayer = floor(random(8, 14)); // Number of leaves in a full circle for the inner layer

  noStroke(); // For a soft, natural look

  // Draw the succulent layers from inside out
  for (let i = 0; i < numLayers; i++) {
    let currentLayerIndex = i;

    // Select color for the current layer from the palette
    let layerColor = colorPalette[currentLayerIndex % colorPalette.length];
    fill(layerColor);

    // Calculate leaf properties for this layer: leaves get longer and wider outwards
    let currentLeafLength = baseLeafLength + currentLayerIndex * layerSpreadFactor * 8;
    let currentLeafWidth = baseLeafWidth + currentLayerIndex * layerSpreadFactor * 3;
    
    // More leaves in outer layers for denser appearance
    let currentNumLeaves = baseLeavesPerLayer + floor(currentLayerIndex * 0.7); 

    // Angle between individual leaves in this layer
    let angleIncrement = 360 / currentNumLeaves;

    push();
    // Apply a rotational offset for each layer to create a spiral effect
    rotate(currentLayerIndex * layerRotationOffset * 0.5);

    // Draw each leaf in the current layer
    for (let j = 0; j < currentNumLeaves; j++) {
      push();
      rotate(j * angleIncrement); // Rotate to position the leaf around the center

      // Translate the leaf outwards from the center.
      // `drawLeaf` draws with its tip at (0,0) and base at (0, length).
      // This translation pushes the leaf's tip away from the central origin.
      translate(0, i * layerSpreadFactor * 6); 

      // Draw the leaf with calculated dimensions
      drawLeaf(currentLeafLength, currentLeafWidth);

      pop();
    }
    pop();
  }

  // Draw a small central bud/core for the succulent
  fill(colorPalette[0]); // Use the lightest yellow for the center
  ellipse(0, 0, baseLeafWidth * 0.8, baseLeafWidth * 0.8);
}

// Function to draw a single succulent leaf shape using bezier curves
// The leaf is drawn with its tip at (0,0) and its base along the positive Y-axis at (0, length).
function drawLeaf(length, width) {
  beginShape();
  // Tip of the leaf
  vertex(0, 0);

  // Right side curve using bezierVertex to create a plump shape
  bezierVertex(
    width * 0.4, length * 0.2,   // Control point 1 (outwards and slightly up)
    width * 0.5, length * 0.7,   // Control point 2 (further outwards and down towards the base)
    0, length                   // End point (base of the leaf)
  );

  // Left side curve (mirrored from the right side)
  bezierVertex(
    -width * 0.5, length * 0.7,  // Control point 1
    -width * 0.4, length * 0.2,  // Control point 2
    0, 0                         // Back to the tip
  );
  endShape(CLOSE);
}

// Uncomment the function below to regenerate a new succulent on mouse click
// function mousePressed() {
//   redraw();
// }