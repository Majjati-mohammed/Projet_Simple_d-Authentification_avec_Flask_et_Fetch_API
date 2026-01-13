async function sendName() {
    const name = document.getElementById("nameInput").value;
    const password = document.getElementById("passInput").value;
    

    const res = await fetch("/CONNECTER", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ name, password })
    });

    const data = await res.json();
    if(data.success){
        window.location.href = "/profile";
    }
    else{
        document.getElementById("result").innerText = data.message;
    }
  }

  async function Inscrire() {
    const name = document.getElementById("name1").value;
    const password = document.getElementById("pass").value;
    const email = document.getElementById("email").value;

    const res = await fetch("/inscrire", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ name, email, password})
    });

    const data = await res.json();
    document.getElementById("result").innerText = data.message;
  }

  async function dash() {

    const resp = await fetch("/api/profile",{
        method: "GET",
    });
    const data = await resp.json();
    if (!resp.ok) {
      const text = await resp.text();
      console.error("Server error:", text);
      return;
    }
    console.log(data.name);
    document.getElementById("username").innerText = data.name;
    document.getElementById("email").innerText = data.mail;
    document.getElementById("date").innerText = data.created_at;
  }
  dash();

  function inscr(){
      window.location.href = "/inscription";
  }

  function connecter(){
    window.location.href = "/";
}

function logout(){
  window.location.href = "/";
}