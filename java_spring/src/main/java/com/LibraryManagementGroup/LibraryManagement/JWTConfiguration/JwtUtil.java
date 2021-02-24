package com.LibraryManagementGroup.LibraryManagement.JWTConfiguration;

import io.jsonwebtoken.*;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

@Service
public class JwtUtil {

    private String SECRET_KEY = "secret";

    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }

    public <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }
    private Claims extractAllClaims(String token) {
        return Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(token).getBody();
    }

    private Boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();
        return createToken(claims, userDetails.getUsername());
    }

    private String createToken(Map<String, Object> claims, String subject) {

        return Jwts.builder().setClaims(claims).setSubject(subject).setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60 * 10))
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY).compact();
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = extractUsername(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }

//    public boolean validateToken(String authToken) throws Exception {
//        try {
//            Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(authToken);
//            return true;
//        } catch (SignatureException ex) {
//            throw new Exception("Invalid JWT signature");
//            return false;
//        } catch (MalformedJwtException ex) {
//            throw new Exception("Invalid JWT token");
//            return false;
//        } catch (ExpiredJwtException ex) {
//            throw new Exception("Expired JWT token");
//            return false;
//        } catch (UnsupportedJwtException ex) {
//            throw new Exception("Unsupported JWT token");
//            return false;
//        } catch (IllegalArgumentException ex) {
//            throw new Exception("JWT claims string is empty.");
//            return false;
//        }
//        return false;
//    }
}
