const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 4000;

app.use(bodyParser.json());

app.post('/publish', (req, res) => {
  try {
    console.log("New product received:", req.body);

    // Check for missing required parameters
    if (!req.body.title) {
      return res.status(400).json({
        status: "error",
        message: "Missing required parameter: title"
      });
    }

    if (!req.body.description) {
      return res.status(400).json({
        status: "error",
        message: "Missing required parameter: description"
      });
    }

    const fakeId = "FAKE_" + Math.floor(Math.random() * 1000000);
    const response = {
      status: "success",
      published_id: fakeId,
      timestamp: new Date().toISOString()
    };

    res.json(response);
  } catch (error) {
    console.error("Error processing request:", error.message);
    res.status(500).json({
      status: "error",
      message: "Failed to process product publishing request",
      error: error.message
    });
  }
});

app.listen(PORT, () => {
  console.log(`📡 Fake product publisher running at http://localhost:${PORT}`);
});
