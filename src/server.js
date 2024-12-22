// server.js
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'dist'))); // Serving the Vue app

app.get('/movie-folders', (req, res) => {
  const movieDir = path.join(__dirname, 'src/assets/movies');
  fs.readdir(movieDir, (err, files) => {
    if (err) {
      return res.status(500).json({ error: 'Failed to read directories' });
    }
    // Filter out non-directory files
    const directories = files.filter(file => fs.statSync(path.join(movieDir, file)).isDirectory());
    res.json(directories);
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
