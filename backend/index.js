let sqlite3 = require("sqlite3").verbose();
let express = require("express");
let http = require("http");

let app = express();
app.use(express.json());
let server = http.createServer(app);
let db = new sqlite3.Database("sqlite.db");

db.run(
  "CREATE TABLE IF NOT EXISTS scores(" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT," +
    "score REAL)"
);

app.get("/api/scores", (request, response) => {
  response.setHeader("contentType", "application/json");
  let type, sql;
  switch (request.query.type) {
    case "highscore":
      type = "highscore";
      sql = "SELECT score score FROM scores ORDER BY score ASC LIMIT 1";
      break;
    case "lowscore":
      type = "lowscore";
      sql = "SELECT score score FROM scores ORDER BY score DESC LIMIT 1";
      break;
    case "average":
      type = "average";
      sql = "SELECT avg(score) score FROM scores";
      break;
    default:
      type = "error";
      break;
  }
  db.serialize(() => {
    db.each(sql, (err, row) => {
      if (err) {
        response.send({ message: "Error encountered while displaying" });
        return console.error(err.message);
      }
      response.send({ type, score: row.score });
    });
  });
});

app.post("/api/scores", (request, response) => {
  db.run("INSERT INTO scores(score) VALUES(?)", [request.body.score], (err) => {
    if (err) {
      return console.log(err.message);
    }
  });
  response.send({ message: "Successful created" });
});

server.listen(3000, function () {
  console.log("Server listening on port: 3000");
});
