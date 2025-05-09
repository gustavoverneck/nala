const query = `
  query {
    app(package: "com.exemplo.app") {
      name
      sdks {
        name
        category
      }
    }
  }
`;

fetch("http://localhost:8000/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query })
})
  .then(res => res.json())
  .then(data => {
    const app = data.data.app;
    const div = document.getElementById("app-info");
    div.innerHTML = `
      <h2>${app.name}</h2>
      <ul>
        ${app.sdks.map(sdk => `<li>${sdk.name} (${sdk.category})</li>`).join('')}
      </ul>
    `;
  })
  .catch(err => console.error("Erro ao buscar dados:", err));
