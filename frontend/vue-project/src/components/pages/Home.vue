<template>
  <div id="container">
    <div id="stage">
      <div id="shape" class=" backfaces cube">
        <div class="plane one"><img class="img-thumbnail" src="https://freeiconshop.com/wp-content/uploads/edd/android-flat.png"></div>
        <div class="plane two">sand</div>
        <div class="plane three"></div>
        <div class="plane four">sand</div>
        <div class="plane five"></div>
        <div class="plane six"><img class="img-thumbnail" src="https://freeiconshop.com/wp-content/uploads/edd/android-flat.png"></div>
        <div class="plane seven"></div>
        <div class="plane eight">box</div>
        <div class="plane nine"></div>
        <div class="plane ten">box</div>
        <div class="plane eleven"></div>
        <div class="plane twelve"></div>
      </div>
    </div>
  <div class="title">
    Android Sandbox
    <div>An Android Sandbox...</div>
  </div>
</div>
</template>
<style type="text/css" media="screen">
  @import url('https://fonts.googleapis.com/css?family=Audiowide');

  #container {
    width: 100%;
    height: 60vh;
    -webkit-perspective: 800;
    /* For compatibility with iPhone 3.0, we leave off the units here */
    -webkit-perspective-origin: 50% 225px;
    color:  #086b18;
  }

  #stage {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    -webkit-transition: -webkit-transform 2s;
    -webkit-transform-style: preserve-3d;
  }

  #shape {
    position: relative;
    margin: 0 auto;
    height: 200px;
    width: 200px;
    -webkit-transform-style: preserve-3d;
  }

  .plane {
    position: absolute;
    height: 200px;
    width: 200px;
    border: 1px dashed #086b18;
    -webkit-box-sizing: border-box;
    font-family: 'Audiowide', cursive;
    font-size: 40pt;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #086b18;
    background-color: #c8ecbd;
    -webkit-transition: -webkit-transform 2s, opacity 2s;
    -webkit-backface-visibility: hidden;
  }

  #shape.backfaces .plane {
    -webkit-backface-visibility: visible;
  }

  #shape {
    -webkit-animation: spin 8s infinite linear;
  }

  @-webkit-keyframes spin {
    from {
      -webkit-transform: rotateY(0);
    }

    to {
      -webkit-transform: rotateY(-360deg);
    }
  }

  /* ---------- cube styles ------------- */
  .cube>.one {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) rotateX(90deg) translateZ(100px);
  }

  .cube>.two {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) rotateY(90deg) translateZ(100px);
  }

  .cube>.three {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) rotateY(180deg) translateZ(100px);
  }

  .cube>.four {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) rotateY(-90deg) translateZ(100px);
  }

  .cube>.five {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) translateZ(100px);
  }

  .cube>.six {
    opacity: 0.5;
    -webkit-transform: scale3d(1.2, 1.2, 1.2) rotateX(-90deg) translateZ(100px) rotate(180deg);
  }

  .cube>.seven {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) rotateX(90deg) translateZ(100px) rotate(180deg);
  }

  .cube>.eight {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) translateZ(100px);
  }

  .cube>.nine {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) rotateY(90deg) translateZ(100px);
  }

  .cube>.ten {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) rotateY(180deg) translateZ(100px);
  }

  .cube>.eleven {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) rotateY(-90deg) translateZ(100px);
  }

  .cube>.twelve {
    -webkit-transform: scale3d(0.8, 0.8, 0.8) rotateX(-90deg) translateZ(100px);
  }

  .title {
    width: 80%;
    height: 15vh;
    box-sizing: border-box;
    margin: 0 auto;
    font-size: 48px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .title div {
    margin: 8px;
    font-size: 24px;
  }

</style>
