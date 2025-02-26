<script>
    let username = "";
    let password = "";
    let message = "";
  
    async function login() {
      message = ""; // Reset message
  
      const response = await fetch("http://127.0.0.1:8000/api/auth/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });
  
      const data = await response.json();
      message = data.message || data.error;
    }
  </script>
  
  <main>
    <h2>Login</h2>
    <input type="text" bind:value={username} placeholder="Username" />
    <input type="password" bind:value={password} placeholder="Password" />
    <button on:click={login}>Login</button>
  
    {#if message}
      <p>{message}</p>
    {/if}
  </main>
  
  <style>
    main {
      width: 300px;
      margin: auto;
      text-align: center;
    }
    input {
      display: block;
      margin: 10px auto;
      padding: 8px;
      width: 100%;
    }
    button {
      padding: 8px;
      background: green;
      color: white;
      border: none;
      cursor: pointer;
    }
  </style>
  