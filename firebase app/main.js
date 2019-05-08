var mainApp = {};

(function(){
    var firebase = app_firebase;
    var uid = null;
    var email = null;
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          // User is signed in.
          uid = user.uid;
          email = user.email;
          console.log(uid);
        }else{
            uid=null;
            window.location.replace('login.html');
        }
      });  
      function logOut(){
        firebase.auth().signOut();
        window.location.replace('login.html');
      
      }
      
      function messageHandler(err){
        if(!!err){
          console.log(err);
        }else{
          console.log('success');
        }
      }
      function fnCreate(){
        var database = firebase.database();
        var ref = database.ref('players/'+uid);
         
        var data = {
            name : email,
            player_score : ball.score_player,
            ai_score : ball.score_ai
        }
        ref.set(data);

      }
      mainApp.logOut = logOut;
      mainApp.fnCreate = fnCreate;
})()
