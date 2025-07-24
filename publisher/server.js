const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 4000;

app.use(bodyParser.json());

app.post('/publish', (req, res) => {
  console.log(" New product received:", req.body);

  const fakeId = "FAKE_" + Math.floor(Math.random() * 1000000);
  const response = {
    status: "success",
    published_id: fakeId,
    timestamp: new Date().toISOString()
  };

  res.json(response);
});

app.listen(PORT, () => {
  console.log(`📡 Fake product publisher running at http://localhost:${PORT}`);
});
