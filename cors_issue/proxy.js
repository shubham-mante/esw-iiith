
const express = require('express');
const request = require('request');

const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

app.get('/test', (req, res) => {
  request(
    { url: 'http://127.0.0.1:8080/~/in-cse/in-name/AE-Test/Data/la',
		headers: {
			'X-M2M-Origin': 'admin:admin',
			'Accept': 'application/json'
		}
},
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: err.message });
      }

      res.json(JSON.parse(body));
    }
  )
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`listening on ${PORT}`));
