const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json());

app.get('/', (req, res) => {
    res.status(200).send({
        message: 'Welcome!'
    });
})

app.listen(PORT, () => {
    console.log(`Server is alive on http://localhost:${PORT}`)
})