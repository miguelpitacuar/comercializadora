import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Products {

  constructor(private httpClient: HttpClient) { }

  getProducts(): Promise<any> {
    return firstValueFrom(this.httpClient.get('http://localhost:8000/api/productos'));
  }
}
