def solution(id_list, k):
    answer = 0

    customer_coupon = {}
    for daily_purchase_history in id_list:
        customer = set([])

        history = daily_purchase_history.split(' ')
        for customer_id in history:
            customer.add(customer_id)

        for customer_id in customer:
            if customer_id not in customer_coupon:
                customer_coupon[customer_id] = 0
            customer_coupon[customer_id] += 1
    
    for num_coupon in customer_coupon.values():
        answer += num_coupon if num_coupon <= k else k

    return answer