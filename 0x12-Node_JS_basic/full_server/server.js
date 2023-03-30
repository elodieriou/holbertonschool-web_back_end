import router from './routes/index'
import express from 'express'

const hostname = '127.0.0.1';
const port = 1245;
const app = express();

app.use('/', router);
app.listen(port, hostname);
export default app;
