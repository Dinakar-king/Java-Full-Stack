import { Component } from '@angular/core';
import { DepartmentFormComponent } from "../department-form/department-form.component";
import { DepartmentTableComponent } from "../department-table/department-table.component";

@Component({
  selector: 'app-department',
  imports: [DepartmentFormComponent,DepartmentTableComponent],
  templateUrl: './department.component.html',
  styleUrl: './department.component.css'
})
export class DepartmentComponent {

}
