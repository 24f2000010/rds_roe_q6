// Function that groups array of objects by 'category' field and sums their 'amount' values
function groupByCategoryAndSum(data) {
    return data.reduce((acc, item) => {
        const category = item.category;
        acc[category] = (acc[category] || 0) + item.amount;
        return acc;
    }, {});
}

// Test with provided data
const testData = [
    {
        "category": "food",
        "amount": 50
    },
    {
        "category": "travel",
        "amount": 100
    },
    {
        "category": "food",
        "amount": 30
    },
    {
        "category": "travel",
        "amount": 75
    }
];

const result = groupByCategoryAndSum(testData);
console.log("Transformed result:", result);
console.log("\nExpected output:");
console.log("{ food: 80, travel: 175 }");

