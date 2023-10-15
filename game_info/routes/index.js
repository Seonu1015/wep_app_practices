var express = require('express');
var router = express.Router();

/* 홈페이지 */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'MindMesh', pageName: 'home/home.ejs'});
});


module.exports = router;
