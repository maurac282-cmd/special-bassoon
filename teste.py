<!DOCTYPE html>
<html>ssss
<head>
  <style>
    /* Estilo do cenário */
    body { background: #222; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    
    /* Criação da bolinha */
    .bola {
      width: 100px;
      height: 100px;
      background-color: crimson;
      border-radius: 50%;
      /* Ativa a animação chamada 'pulsar' que dura 2 segundos e se repete para sempre */
      animation: pulsar 2s infinite alternate ease-in-out;
    }

    /* O que a animação faz ao longo do tempo */
    @keyframes pulsar {
      0% { transform: scale(0.8); background-color: crimson; }
      100% { transform: scale(1.3); background-color: gold; box-shadow: 0 0 30px gold; }
    }
  </style>
</head>
<body>
  <div class="bola"></div>
</body>
</html>