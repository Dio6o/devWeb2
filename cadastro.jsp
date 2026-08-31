<%@ page import="java.util.*, model.*" %>
<%
    ArrayList<Animal> lista = (ArrayList<Animal>) application.getAttribute("lista");
    if (lista == null) {
        lista = new ArrayList<Animal>();
        application.setAttribute("lista", lista);
    }

    if ("POST".equalsIgnoreCase(request.getMethod())) {
        String tipo = request.getParameter("tipo");
        String nome = request.getParameter("nome");
        Animal a = null;

        if ("cachorro".equals(tipo)) {
            a = new Cachorro(nome);
        } else if ("gato".equals(tipo)) {
            a = new Gato(nome);
        } else if ("passaro".equals(tipo)) {
            a = new Passaro(nome);
        }

        if (a != null) {
            lista.add(a);
        }
    }
%>
<html>
<body>

<h2>Cadastro de Animais</h2>

<form method="post" action="cadastro.jsp">
    Nome: <input type="text" name="nome" required><br>
    Tipo:
    <select name="tipo">
        <option value="cachorro">Cachorro</option>
        <option value="gato">Gato</option>
        <option value="passaro">Passaro</option>
    </select><br>
    <input type="submit" value="Cadastrar">
</form>

<h3>Animais cadastrados</h3>
<ul>
<%
    for (Animal an : lista) {
%>
    <li><%= an.getNome() %> (<%= an.getClass().getSimpleName() %>) - Som: <%= an.emitirSom() %></li>
<%
    }
%>
</ul>

</body>
</html>
