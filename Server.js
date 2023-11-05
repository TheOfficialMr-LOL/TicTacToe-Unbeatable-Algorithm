//link to website: http://localhost:2000/
//c:\Users\rjini\OneDrive\Desktop\TicTacToe_Web_Version\images

//Importing the libraries required
const {spawn}=require("child_process");
var ports=[];

var fs=require("fs");
var express=require("express");
var app=express();
app.use(express.json());
const port = process.env.port || 2000;

//Intitalising the location of the files
var publicDir_Images=require("path").join(__dirname, "/images");
var publicDir_Audio=require("path").join(__dirname, "/audio");
app.use(express.static(publicDir_Images));
app.use(express.static(publicDir_Audio));


//Initialising the server
app.use("/", (req, res) => {

    //Detecting requests sent to the server
    if (req.method=="POST") {
        if (req.url=="/data") {
            gameBoard=req.body.mainBoard;
            gameBoard=gameBoard.toString();
            console.log("The request to generate the game board was recieved!");

            var pyProg=spawn("python", ["TicTacToeAlgorithm_WebVersion.py", gameBoard]);  
            pyProg.stdout.on("data", (data) => {

                console.log(data);
                GameBoard=data.toString()
                console.log(GameBoard, "Hello");
                res.send(GameBoard);
                console.log("The game board was sent to the client")
            });
        }




        if(req.url=="/session_Generting_Request") {
            console.log("The request to generate the session has been recieved!");
            port_num=generate_session().toString();
            res.send(port_num);
            console.log("The port number was sent to the client!");
        }
    }



    

    if (req.url=="/") {
        fs.readFile("index.html", function(err, data) {
            console.log("Reading index.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()

        });
    }
    if (req.url=="/index.html") {
        fs.readFile("index.html", function(err, data) {
            console.log("Reading index.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()

        });
    }
    if (req.url=="/PlayerVSComputer.html") {
        fs.readFile("PlayerVSComputer.html", function(err, data) {
            console.log("Reading PlayerVSComputer.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()

        });
    }
    if (req.url=="/RemoteGame.html") {
        fs.readFile("RemoteGame.html", function(err, data) {
            console.log("Reading RemoteGame.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()

        });
    }
    if (req.url=="/LocalGame.html") {
        fs.readFile("LocalGame.html", function(err, data) {
            console.log("Reading LocalGame.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()
        });
    }
    if (req.url=="/UI_Test.html") {
        fs.readFile("UI_Test.html", function(err, data) {
            console.log("Reading UI_Test.html");
            res.writeHead(200, {"Content-Type": "text/html"});
            res.write(data);
            return res.end()
        });
    }



});



app.listen(port, function() {

    console.log("Connected to port " + port);

});


function generate_session(req,res) {

    max=9999;
    min=1000;
    port_num=Math.floor(Math.random()*(max-min))+min;

    //Checking if the port number doesn't already exist
    while (ports.includes(port_num)==true) {
        port_num=Math.floor(Math.random()*(max-min))+min;
    }
    ports.push(port_num);
    return port_num;
}

