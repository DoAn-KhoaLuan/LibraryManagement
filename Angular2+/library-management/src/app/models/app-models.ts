export class filter_page {
    page: number;
    perPage: number;
}


export class account {
    account_id: string | number;
    role: any;
    account_name: string
}

export class Account {
    account_id: string | number;
    role: any;
    account_name: string;
}
export class auth_info {
    accessToken: string;
    account: any;
    user_info: any;
}

export class order_line {
  book_id: string;
  image: string;
  name: string;
  quantity: number;
  retailPrice:  number;
  new_amount: number;
  total_price:  number;
  discount: number;
}

export class Message {
    conversation_id: string | Number;
    content: any;
    account_id: string | Number;
    created_at: Date;
    deleted_at: Date;
    type: string;
}

export class Conversation {
    conversation_id: string | Number;
    account: Account;
    customer_account_id: Number | string;
    last_message: string;
    updated_at: Date;
    messages: Message[] = [];
    is_read: boolean = false;
    current_page: Number;
}
