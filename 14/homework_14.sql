--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cars; Type: TABLE; Schema: public; Owner: PTLam
--

CREATE TABLE public.cars (
    id uuid NOT NULL,
    name character varying(50) NOT NULL,
    model_uid uuid,
    manufacturer_uid uuid
);


ALTER TABLE public.cars OWNER TO "PTLam";

--
-- Name: manufactures; Type: TABLE; Schema: public; Owner: PTLam
--

CREATE TABLE public.manufactures (
    id uuid NOT NULL,
    name character varying(50) NOT NULL,
    country character varying(50) NOT NULL,
    year_of_foundation date NOT NULL,
    telephone integer,
    email character varying(100)
);


ALTER TABLE public.manufactures OWNER TO "PTLam";

--
-- Name: models; Type: TABLE; Schema: public; Owner: PTLam
--

CREATE TABLE public.models (
    id uuid NOT NULL,
    model character varying(100) NOT NULL,
    year_of_issue date NOT NULL,
    price numeric(19,2) NOT NULL,
    class character varying(1) NOT NULL,
    number_of_seats integer NOT NULL,
    engine_dispacement integer NOT NULL,
    capacity integer NOT NULL,
    CONSTRAINT models_class_check CHECK ((((class)::text = 'A'::text) OR ((class)::text = 'B'::text) OR ((class)::text = 'C'::text))),
    CONSTRAINT models_price_check CHECK ((price > (0)::numeric))
);


ALTER TABLE public.models OWNER TO "PTLam";

--
-- Data for Name: cars; Type: TABLE DATA; Schema: public; Owner: PTLam
--

COPY public.cars (id, name, model_uid, manufacturer_uid) FROM stdin;
b30ed52a-2c21-4459-8fc3-df6c4cd9292f	Suzuki_1	f123e6db-a87a-42ce-aa6e-ad939c21b86e	a8adbac3-5728-4874-9648-777fc48ecda9
8a115962-4add-4298-85f0-2747d6c3110b	Suzuki_2	8249b76a-ac76-4b24-bf95-0e29b4e4b3f5	a8adbac3-5728-4874-9648-777fc48ecda9
bcee7b01-ad24-4a87-bb27-ddb49baf3dd7	Suzuki_3	eeb7c5e9-3bef-449e-ac49-6fe8ee0d4c0e	a8adbac3-5728-4874-9648-777fc48ecda9
fe8b71df-852a-41c4-b569-749769104a7e	Jeep_1	4980f454-aa61-45a4-a14a-3fe288dc05c0	b6189605-2501-4758-ad7c-e40dc27b2172
d80559fd-46b7-463d-b661-8f632ae2bbd5	Jeep_2	dd180693-35f5-41d7-a4c1-b8d61cd48734	b6189605-2501-4758-ad7c-e40dc27b2172
d627740a-2841-4296-91d7-6b3248cffa65	Jaguar_1	ee1cd73b-0d2d-4446-abff-a7b06d7ddc0e	dc263710-57db-4ade-8495-7374cd2d542a
\.


--
-- Data for Name: manufactures; Type: TABLE DATA; Schema: public; Owner: PTLam
--

COPY public.manufactures (id, name, country, year_of_foundation, telephone, email) FROM stdin;
a8adbac3-5728-4874-9648-777fc48ecda9	Suzuki	Japan	1909-10-01	80050525	suzuki@gmail.com
b6189605-2501-4758-ad7c-e40dc27b2172	Jeep	USA	1941-01-01	90150514	jeep@gmail.com
dc263710-57db-4ade-8495-7374cd2d542a	Jaguar	UK	1922-09-02	\N	\N
\.


--
-- Data for Name: models; Type: TABLE DATA; Schema: public; Owner: PTLam
--

COPY public.models (id, model, year_of_issue, price, class, number_of_seats, engine_dispacement, capacity) FROM stdin;
f123e6db-a87a-42ce-aa6e-ad939c21b86e	Aerio 1.5	2003-10-10	10000.00	A	4	1491	110
8249b76a-ac76-4b24-bf95-0e29b4e4b3f5	Aerio 1.8	2005-11-21	15000.00	A	4	1796	125
eeb7c5e9-3bef-449e-ac49-6fe8ee0d4c0e	Aerio 1.8 4WD	2006-04-02	25000.00	A	4	2290	155
4980f454-aa61-45a4-a14a-3fe288dc05c0	Chorokee	2013-11-01	35000.00	B	5	1968	170
dd180693-35f5-41d7-a4c1-b8d61cd48734	Commander	2010-10-01	30000.00	C	5	2987	217
ee1cd73b-0d2d-4446-abff-a7b06d7ddc0e	E-Pace	2017-05-02	20000.00	A	4	1999	150
\.


--
-- Name: cars cars_pkey; Type: CONSTRAINT; Schema: public; Owner: PTLam
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_pkey PRIMARY KEY (id);


--
-- Name: manufactures manufactures_pkey; Type: CONSTRAINT; Schema: public; Owner: PTLam
--

ALTER TABLE ONLY public.manufactures
    ADD CONSTRAINT manufactures_pkey PRIMARY KEY (id);


--
-- Name: models models_pkey; Type: CONSTRAINT; Schema: public; Owner: PTLam
--

ALTER TABLE ONLY public.models
    ADD CONSTRAINT models_pkey PRIMARY KEY (id);


--
-- Name: cars cars_manufacture_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: PTLam
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_manufacture_uid_fkey FOREIGN KEY (manufacturer_uid) REFERENCES public.manufactures(id);


--
-- Name: cars cars_model_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: PTLam
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_model_uid_fkey FOREIGN KEY (model_uid) REFERENCES public.models(id);


--
-- PostgreSQL database dump complete
--

