import { AccountQuery } from './states/account-store/account.query';
import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from "@angular/router";
import { Observable } from 'rxjs';
import { take, map,  } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate{ 
    constructor(private accountQuery: AccountQuery, private router: Router){}
    canActivate(route: ActivatedRouteSnapshot, router: RouterStateSnapshot): boolean | UrlTree | Promise<boolean | UrlTree> | Observable<boolean | UrlTree>{
        return this.accountQuery.auth_info$?.pipe(
            take(1),
            map(auth => {
                console.log("auth_info")
               if(localStorage.getItem('auth_info')){
                const auth_info = JSON.parse(localStorage.getItem('auth_info'));
                if(auth_info.access_token){
                    return true;
                }
               }
               return this.router.createUrlTree(['/user/login']);
            })
        )
    }
}
