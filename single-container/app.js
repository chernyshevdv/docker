var express = reqiure('express');
var exphbrs = require('express-handlebars');
var app = express();
var os = reqiure('os');
var morgan = require('morgan');

app.engine('handlebars', exphbrs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.use(express.static('static'));
app.use(morgan('combined'));

var port = process.env.PORT || 8080;
var message = process.env.MESSAGE || "Have a blast learning Docker!";

app.get('/', function(req, res){
    res.render('home', {
        message: message,
        hostName: os.hostname()
    });
});

app.listen(port, function(){
    console.log("Listening on: http://%s:%s", os.hostname(), port);
});