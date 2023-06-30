var audio = new Audio();
    function playMusic(musicFileURL) {
      audio.src = musicFileURL;
      audio.play();
    }

      function stopMusic() {
        audio.pause();
        audio.currentTime = 0;
      }
  
      function increaseVolume() {
        if (audio.volume < 1.0) {
          audio.volume += 0.1;
        }
      }
      function decreaseVolume(){
        if(audio.volume>0.0){
          audio.volume -=0.1
        }
      }
/*------------------------------------------------------------------------------------------------------------------------*/


