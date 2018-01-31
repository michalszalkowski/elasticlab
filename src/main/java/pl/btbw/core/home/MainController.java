package pl.btbw.core.home;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {

    private static final Logger LOGGER = LoggerFactory.getLogger(MainController.class);

    @RequestMapping("/")
    public Response simulation(@RequestParam(value = "type", defaultValue = "XSS attack detect") String type) {
        LOGGER.error("[SECURITY EVENT] {}", type);
        return new Response(type);
    }

    @RequestMapping("/message")
    public Response simulationError(@RequestParam(value = "message", defaultValue = "ERROR") String message) {
        LOGGER.error("{}", message);
        return new Response(message);
    }

}
