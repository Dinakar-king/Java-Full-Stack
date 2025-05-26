import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EmployeeService } from '../../services/employee.service';
import { Employee } from '../../models/employee';

@Component({
  selector: 'app-employee-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './employee-table.component.html',
  styleUrls: ['./employee-table.component.css']
})
export class EmployeeTableComponent {
  employees: Employee[] = [];
  loading = false;
  error = '';

  constructor(private employeeService: EmployeeService) {}

  loadEmployees(): void {
    this.loading = true;
    this.error = '';
    this.employeeService.getEmployees().subscribe({
      next: data => {
        this.employees = data;
        this.loading = false;
      },
      error: err => {
        this.error = 'Failed to fetch employees';
        this.loading = false;
      }
    });
  }
}
