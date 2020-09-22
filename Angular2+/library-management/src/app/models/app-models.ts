export class filter_page {
    page: number;
    per_page: number
}


export class account {
    role: any;
    account_name: string
}

export class auth_info {
    access_token: string;
    current_account: any;
    user_info: any;
}

export class order_line {
  book_id: string;
  image: string;
  book_name: string;
  quantity: number;
  retail_price:  number;
  new_amount: number;
  total_price:  number;
  discount: number;
}
