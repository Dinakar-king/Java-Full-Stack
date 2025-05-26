import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DepartmentService } from '../../services/department.service';
import { Department } from '../../models/department';

@Component({
  selector: 'app-department-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './department-table.component.html',
  styleUrls: ['./department-table.component.css']
})
export class DepartmentTableComponent {
loaddepartment() {
throw new Error('Method not implemented.');
}
  departments: Department[] = [];
  loading = false;
  error = '';

  constructor(private departmentService: DepartmentService) {}

  loadDepartments(): void {
    this.loading = true;
    this.error = '';
    this.departmentService.getDepartments().subscribe({
      next: data => {
        this.departments = data;
        this.loading = false;
      },
      error: err => {
        this.error = 'Failed to fetch departments';
        this.loading = false;
      }
    });
  }
}
