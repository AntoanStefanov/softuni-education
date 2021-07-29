function solve(input) {
    const campaignDays = Number(input[0]);
    const cookers = Number(input[1]);
    const cakes = Number(input[2]);
    const guffrets = Number(input[3]);
    const pancakes = Number(input[4]);

    const collectedSumForDay = (cakes * 45 + guffrets * 5.80 + pancakes * 3.20) * cookers;
    const collectedSumForCampaign = collectedSumForDay * campaignDays;
    const clearMoney = collectedSumForCampaign - (collectedSumForCampaign/ 8);
    console.log(clearMoney);
}

solve(['23', '8', '14', '30', '16']);