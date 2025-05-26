export interface Employee {
  id: number;
  name: string;
  email: string;
  position?: string;
  departmentId?: number;
  hireDate?: string; // LocalDate serialized as ISO string
}