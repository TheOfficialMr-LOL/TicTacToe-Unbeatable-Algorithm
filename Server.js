//link to website: http://localhost:8080/
//c:\Users\rjini\OneDrive\Desktop\TicTacToe_Web_Version\images

const {spawn}=require("child_process");

var http=require("http");
var fs=require("fs");
var qs=require("querystring");
var url=require("url");
var express=require("express");
var app=express();
app.use(express.json());

var publicDir=require("path").join(__dirname, "/images");
app.use(express.static(publicDir));

var events=require("events");
//C:/Users/rjini/OneDrive/Desktop/TicTacToe_Web_Version/Test.py


app.use("/", (req, res) => {


    if (req.method=="POST") {

        gameBoard=req.body.mainBoard;
        gameBoard=gameBoard.toString();
        console.log("The request to generate the game board was recieved!");

        var pyProg=spawn("python", ["TicTacToeAlgorithm_WebVersion.py", gameBoard]);  
        pyProg.stdout.on("data", (data) => {

            console.log(data);
            GameBoard=data.toString()
            console.log(GameBoard);
            res.send(GameBoard);
            console.log("The game board was sent to the client")
            
        });
    }

    if (req.url=="/") {
        fs.readFile("index.html", function(err, data) {
            console.log("Reading file");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()

        });
    }
});


    
app.listen(8080, function() {

    console.log("Connected to port 8080");

});
