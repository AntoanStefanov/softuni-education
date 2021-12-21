
function solution(S, K) {
    const DAYS_IN_WEEK = 7;
    let weekDays = { 0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun' };
    function getValueByDay(weekDays, value) {
        return +Object.keys(weekDays).find(key => weekDays[key] === value);
    }

    let currentDayValue = getValueByDay(weekDays, S);
    let nextDayValue = (currentDayValue + K) % DAYS_IN_WEEK;

    return weekDays[nextDayValue];
}

solution('Wed', 2);
solution('Sat', 23);
