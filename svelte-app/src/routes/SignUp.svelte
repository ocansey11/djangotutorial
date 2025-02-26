<script>
  let username = "";
  let password = "";
  let message = "";

  async function signup() {
    message = ""; // Reset message

    const response = await fetch("http://127.0.0.1:8000/accounts/signup/", {
      method: "POST",  // ✅ Make sure it's POST
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })  // ✅ Send data in request body
    });

    const data = await response.json();
    message = data.message || data.error;  // ✅ Display success or error message
  }
</script>

<main>
  <h2>Sign Up</h2>
  <input type="text" bind:value={username} placeholder="Username" />
  <input type="password" bind:value={password} placeholder="Password" />
  <button on:click={signup}>Sign Up</button>

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
    background: blue;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>
