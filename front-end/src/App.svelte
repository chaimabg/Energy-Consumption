<script lang="ts">
  import EnergyConsumption from './EnergyConsumption.svelte'
  let date='';
  let error='';
  const maxDate='2022-05-31';
  const minDate='2020-01-01';
  let consumptions=[];
  function FindConsumption(){
    consumptions=[];
    if (date<minDate || date>maxDate){
      error='Incorrect Date, Choose date between '+ maxDate+ ' and '+ minDate;
    }else{
      error='';
      fetch(`http://localhost:5000/get?date=${date}`)
              .then(response => response.json())
              .then(data => {
                consumptions=data.response;
              }).catch(err => {
        error = 'Request Error: Try again ! '
      });
    }
  }
</script>

<main>
  <h1>Energy Consumption in France</h1>

  <section>
    <hr>
    {#if error}
      <p class="error">{error}</p>
    {/if}
    <div>
      <label for="date">Choose a Date</label>
      <input type="date" id="date"  max={maxDate} min={minDate}  bind:value={date}/>
    </div>
    <button on:click={FindConsumption}> Search</button>
    <hr>
  </section>

  {#if !error}
    <EnergyConsumption date={date} consumptions={consumptions}></EnergyConsumption>
  {/if}

</main>

<style>
  .read-the-docs {
    color: #888;
  }
  h1 {
    color: #ff3e00aa;
  }
  button{
    font : larger;
    padding: 0.15rem 0.5rem;
    width: 50%;
    height: 30px;
    background-color: #1b1a1a;
    border: 1px solid  aliceblue ;
    cursor: pointer;
    color: white;
  }
  .error{
    color: #cd2f2f;
    background-color: rgba(255, 0, 0, 0.24);
    width: 100%;
    font-weight: 450;
    padding: 5px;
  }
  label,input{
    width: 75%;
    height: 30px;
    margin: 5px;
  }
</style>
