{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hei, {{ name }}
{% endblock %}

{% block html %}
<style>
th{
    width: 120px;

}
td{
    text-align: center;
}
</style>
<h2>Takk for bestillingen. </h2>
Jeg nå har lagret følgende om din bestilling.
<h3>Kontaktinformasjon</h3>
<strong>Navn:</strong> {{ name}} {{lastName}} <br>
<strong>Epost:</strong> {{ email}} <br>
<strong>Tlf:</strong> {{ phone }} <br>
<h3>Planter</h3>
<table class="table">
  <thead class="thead-dark">
  <tr>
    <th scope="col">#</th>
    <th scope="col">Plante Navn</th>
    <th scope="col">Størrelse</th>
    <th scope="col">Antall</th>
    <th scope="col">Pris*</th>
  </tr>
  </thead>
  <tbody>
  {% for o in listOfPlants %}
    <tr>
      <th scope="row">{{ forloop.counter }}</th>
      <td>{{ o.plant_name }}</td>
      <td>{{ o.size }}</td>
      <td>{{ o.amount }}</td>
      <td>{{ o.price }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
<hr>
*Norsk moms, frakt og andre avgifter vil komme i tillegg. <br>
Alle planter skal hentes hjemme hos meg. <br> <br>

Har du noen spørsmål? Kontakt meg på jo.engen@gmail.com. <br>  <br>  <br>
Med vennlig hilsen,  <br>
Johnny Engen <br>
jo.engen@gmail.com <br><br>
<strong>NB: Denne er en automatisk generert epost. Ikke svar.</strong>
{% endblock %}