<script>
    export let consumptions;
    export let date;
</script>

<main>
    {#if consumptions.length }
    <h1>Energy Consumption for the date {date}</h1>
        <div>
            <table>
                <tr>
                    <th>Hour</th>
                    <th>Consumption (MW)</th>
                    <th>Forecasting D-1</th>
                    <th>Forecasting D</th>
                </tr>

                {#each consumptions as {  hour, consumption , forecastingD_1,forecastingD,id}, i}
                    <tr>
                        <td>{hour}</td>
                        <td>{consumption}</td>
                        <td>{forecastingD_1}</td>
                        <td>{forecastingD}</td>
                    </tr>
                {/each}
            </table>
        </div>


        {/if}
</main>


<style>
    div{
        margin: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.26);
        max-height:350px;
        overflow: auto;
    }
    h1{
        font-size: 1.25rem;
        margin: 0.25rem 0;
    }

    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;

    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: rgba(243, 240, 240, 0.42);
    }
</style>
