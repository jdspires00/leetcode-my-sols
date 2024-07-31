/**
 * Definition for singly-linked list.
 */
//  Solution takes 99ms and beats 85.89% and uses 55.20 MB of memory beating 80.54% as of 7/31/2024 
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
 }
 
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummyHead = new ListNode(0);
    let current = dummyHead;
    let carry = 0;
    let p = l1;
    let q = l2;

    while (p !== null || q !== null) {
        const x = (p !== null) ? p.val : 0;
        const y = (q !== null) ? q.val : 0;
        const sum = carry + x + y;
        carry = sum > 9 ? 1 : 0;
        current.next = new ListNode(sum % 10);
        current = current.next;
        if (p !== null) p = p.next;
        if (q !== null) q = q.next;
    }

    if (carry > 0) {
        current.next = new ListNode(carry);
    }

    return dummyHead.next;
}

// Helper function to create a linked list from an array
function createLinkedList(arr) {
    let dummyHead = new ListNode(0);
    let current = dummyHead;
    for (let val of arr) {
        current.next = new ListNode(val);
        current = current.next;
    }
    return dummyHead.next;
}

// Helper function to convert a linked list to an array
function linkedListToArray(head) {
    let arr = [];
    while (head) {
        arr.push(head.val);
        head = head.next;
    }
    return arr;
}

// Test the solution
const solution = addTwoNumbers;
