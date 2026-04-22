Table users{
  user_id integer [primary key]
  username varchar
  email varchar
  password varchar
  role enum("Front Desk" , "Manager" , "Tenant", "Finance", "Maintenance" , "Admin")
  location_id varchar [ref: > locations.location_id, null]
}

Table tenants{
  tenant_id integer [primary key]
  user_id integer [ref: - users.user_id]
  first_name varchar
  last_name varchar
  national_insurance varchar
  phone_number string
  occupation varchar
  references varchar
  requirements varchar
}

Table apartments{
  apartment_id integer [primary key]
  location_id varchar [ref: > locations.location_id]
  room_type varchar 
  monthly_rent decimal 
  bedrooms integer 
  bathrooms integer
  occupancy_status boolean
}

Table locations{
  location_id varchar [primary key]
  location_name varchar 
  location_manager int [ref: - users.user_id]
}

Table contracts{
  contract_id integer [primary key]
  apartment_id integer [ref: > apartments.apartment_id]
  tenant_id integer [ref: > tenants.tenant_id]
  start_date datetime 
  end_date datetime 
  payment_frequency enum("Weekly", "Monthly" , "Annually")
  early_leave boolean
  penalty_amount decimal
}

Table payment_schedule{
  schedule_id integer [primary key]
  contract_id integer [ref: > contracts.contract_id]
  due_date datetime
  amount_due decimal 
  status enum("Completed" , "Scheduled", "Unpaid")
}

Table payments{
  payment_id integer [primary key]
  schedule_id integer [ref: - payment_schedule.schedule_id]
  payment_date datetime
  amount_paid decimal 
  payment_status enum("Scheduled" ,"Unpaid" , "Completed")
  method enum("Direct Debit" , "Bank Transfer" , "Cash")
  reference varchar
}

Table invoices{
  invoice_id integer [primary key]
  contract_id integer [ref: > contracts.contract_id]
  schedule_id integer [ref: - payment_schedule.schedule_id]
  issued_date datetime
  due_date datetime
  amount decimal
  status enum("Scheduled", "Completed")
}

Table maintenance_requests{
  request_id integer [primary key]
  tenant_id integer [ref: > tenants.tenant_id]
  apartment_id integer [ref: > apartments.apartment_id]
  description varchar
  priority enum("High","Medium","Low")
  status enum("Scheduled","Completed", "Pending")
  maintenance_notes varchar
  scheduled_date datetime
  resolved_date datetime
  time_taken int
  cost decimal
}

Table complaints{
  complaint_id integer [primary key]
  tenant_id integer [ref: > tenants.tenant_id]
  tenant_message varchar
  created_at datetime 
  resolved_at datetime
}

Table notifications{
  notification_id integer [primary key]
  tenant_id integer [ref: > tenants.tenant_id]
  type enum("Urgent","Reminder")
  message varchar
  is_read boolean 
  created_at datetime
}
