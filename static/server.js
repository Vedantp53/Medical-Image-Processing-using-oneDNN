const express = require('express');
const multer = require('multer');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/upload', upload.single('fileInput'), (req, res) => {
  const filePath = req.file.path;
  
  // Here, you can process the file and generate a preview image or perform other operations
  
  res.json({ filePath: filePath });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});