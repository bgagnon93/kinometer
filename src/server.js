// server.js
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files
app.use(express.static(path.join(__dirname, '../dist')));

// API endpoint to get movie folders
app.get('/api/movie-folders', (req, res) => {
  const movieDir = path.join(__dirname, '../public/assets/movies');
  fs.readdir(movieDir, (err, files) => {
    if (err) {
      return res.status(500).json({ error: 'Failed to read directories' });
    }
    // Filter out non-directory files
    const directories = files.filter(file => fs.statSync(path.join(movieDir, file)).isDirectory());
    res.json(directories);
  });
});

// Setup routes for different sorting endpoints
const endpoints = ['bg', 'jw', 'title', 'year'];

// Add routes for each endpoint
endpoints.forEach(endpoint => {
  app.get(`/${endpoint}`, (req, res) => {
    res.sendFile(path.join(__dirname, '../dist/index.html'));
  });
});

// Catch-all route to serve the Vue app for any other request
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../dist/index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
