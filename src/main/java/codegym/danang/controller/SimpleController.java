package codegym.danang.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SimpleController {


 
	@RequestMapping("/")
    public String homePage(Model model) {

        return "/fragments/p1";
    }


}
