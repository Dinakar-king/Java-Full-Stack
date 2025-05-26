import { Component } from '@angular/core';
import { EmployeeFormComponent } from "../employee-form/employee-form.component";
import { EmployeeTableComponent } from "../employee-table/employee-table.component";

@Component({
  selector: 'app-employee',
  imports: [EmployeeFormComponent, EmployeeTableComponent],
  templateUrl: './employee.component.html',
  styleUrl: './employee.component.css'
})
export class EmployeeComponent {

}
