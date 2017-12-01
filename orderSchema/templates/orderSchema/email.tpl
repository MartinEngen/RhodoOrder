{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
Takk for bestillingen. <br>
Jeg har lagret følgende om din bestilling:
<table class="table">
  <thead class="thead-dark">
  <tr>
    <th scope="col">#</th>
    <th scope="col">Plante Navn</th>
    <th scope="col">Antall</th>
    <th scope="col">Pris</th>
  </tr>
  </thead>
  <tbody>
  {% for o in listOfPlants %}
    <tr>
      <th scope="row">{{ forloop.counter }}</th>
      <td>{{ o.plant_name }}</td>
      <td>{{ o.amount }}</td>
      <td>{{ o.price }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

Pris (ekskl. mva): {{ priceTotal }}
{% endblock %}